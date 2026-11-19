from ptcgo.game.card_effects.support_common import switch_self_attack
from ptcgo.game.content.definitions import evolves_from
from ptcgo.game.data_utils import PokemonCardDef, Attack
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def _valiant_evolution_then(ctx, new_active):
    pokemon = ctx.source
    logic_name = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)

    def eligible(card):
        return bool(logic_name) and evolves_from(
            getattr(card, "archetype_id", None) or "", logic_name)

    picks = await ctx.search_deck(
        eligible, count=1, minimum=0,
        prompt="Choose an Evolution card for this Pok\u00e9mon")
    if picks:
        await ctx.evolve_pokemon(pokemon, picks[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="b092b28c-6460-56c6-ba14-5655fabb36c2",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name",
    display_name="Finizen",
    searchable_by=["Finizen", "Basic", "Finizen"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=963,
    abilities=[
        Attack(
            title="Valiant Evolution",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. If you do, search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=switch_self_attack(then=_valiant_evolution_then),
        ),
        Attack(
            title="Razor Fin",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
