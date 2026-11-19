from ptcgo.game.attributes import AttrID
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.pokemon import is_psychic_energy
from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.content.definitions import Activations
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def psy_shadow_condition(board, player_id, pokemon):
    if pokemon is None or pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    deck = board.find_player_area(player_id, "deck")
    return bool(deck) and any(is_psychic_energy(card) for card in deck.children)


async def psy_shadow(ctx):
    attached = await search_attach_energy(
        is_psychic_energy, count=1, to_self=False,
        prompt="Search your deck for a Psychic Energy card and attach it",
    )(ctx)
    if not attached:
        return 0
    target = attached[0][1] if isinstance(attached[0], tuple) else None
    if target is None:
        return await ctx.place_damage_counters(2)
    await ctx.deal_damage(20, target=target, apply_modifiers=False, as_counters=True)
    return 1

card = PokemonCardDef(
    guid="fc4da42d-5580-518c-b561-f13176806f4b",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name",
    display_name="Gardevoir",
    searchable_by=["Gardevoir", "Stage 2", "Gardevoir"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="EX1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Psy Shadow",
            game_text="Once during your turn (before your attack), you may search your deck for a Psychic Energy card and attach it to 1 of your Pok\u00e9mon. Put 2 damage counters on that Pok\u00e9mon. Shuffle your deck afterward. This power can't be used if Gardevoir is affected by a Special Condition.",
            effect=psy_shadow,
            activation=Activations.ONCE_PER_TURN,
            condition=psy_shadow_condition,
        ),
        Attack(
            title="Energy Burst",
            game_text="Does 10 damage times the total amount of Energy attached to Gardevoir and the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)