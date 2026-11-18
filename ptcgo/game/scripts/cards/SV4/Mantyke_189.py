from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bfa2ea08-6889-5276-854a-3be94d3574bf",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mantyke.Name",
    display_name="Mantyke",
    searchable_by=["Mantyke", "Basic", "Mantyke"],
    subtypes=["Basic"],
    collector_number=189,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=458,
    abilities=[
        Attack(
            title="Buoyant Healing",
            game_text="Heal 120 damage from 1 of your Benched Pok\u00e9mon.",
            cost={},
            effect=unimplemented,
        ),
    ],
)