from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.card_effects.attacks_common import named_in_play
from ptcgo.game.content.definitions import evolves_from
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

_PARTNER_IN_PLAY = named_in_play("Shelmet", side="both")


async def _mysterious_evolution(ctx):
    """With the partner in play, search the deck for the card that evolves
    directly from this Pokemon and put it onto this Pokemon (an evolution)."""
    if not _PARTNER_IN_PLAY(ctx):
        return
    pokemon = ctx.attacker
    if pokemon is None:
        return
    logic_name = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    if not logic_name:
        return
    stage = pokemon.get_attribute(AttrID.STAGE)

    def _direct_evolution(card):
        if not evolves_from(getattr(card, "archetype_id", None) or "", logic_name):
            return False
        return stage is None or card.get_attribute(AttrID.STAGE) == stage + 1

    picks = await ctx.search_deck(_direct_evolution, count=1, minimum=0,
                                  prompt="Choose an Evolution card")
    if picks:
        await ctx.evolve_pokemon(pokemon, picks[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="05856e61-af17-522d-bc84-f208c4ac8a11",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name",
    display_name="Karrablast",
    searchable_by=["Karrablast", "Basic", "Karrablast"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="BW3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=588,
    abilities=[
        Attack(
            title="Mysterious Evolution",
            game_text="If Shelmet is in play, search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon. (This counts as evolving this Pok\u00e9mon.) Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_mysterious_evolution,
        ),
        Attack(
            title="Fury Attack",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=10),
        ),
    ],
)