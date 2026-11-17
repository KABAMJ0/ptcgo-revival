from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4ae36c2f-9e05-5d07-b11a-5c7c73beaff1",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name",
    display_name="Charjabug",
    searchable_by=["Charjabug", "Stage 1", "Charjabug"],
    subtypes=["Stage 1"],
    collector_number=169,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grubbin.Name",
    family_id=736,
    abilities=[
        Attack(
            title="Static Shock",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=60,
        ),
    ],
)