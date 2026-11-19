from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import search_attach_energy


card = PokemonCardDef(
    guid="87f7f48c-25f3-5a5f-91c9-822e823d5cd2",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name",
    display_name="Fletchinder",
    searchable_by=["Fletchinder", "Stage 1", "Fletchinder"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchling.Name",
    family_id=661,
    abilities=[
        Attack(
            title="Flame Charge",
            game_text="Search your deck for a Fire Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=search_attach_energy(predicate=lambda c: energy_provides_type(c, PokemonTypes.FIRE.value), count=1, to_self=True, prompt='Choose a Fire Energy card to attach.'),
        ),
    ],
)