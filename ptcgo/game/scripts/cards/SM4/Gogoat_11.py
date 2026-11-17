from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3e940188-dae2-5a82-9e4a-ddb4baea2efb",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gogoat.Name",
    display_name="Gogoat",
    searchable_by=["Gogoat", "Stage 1", "Gogoat"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="SM4",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skiddo.Name",
    family_id=672,
    abilities=[
        Ability(
            title="Sap Sipper",
            game_text="This Pok\u00e9mon's attacks do 80 more damage to your opponent's Grass Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Horn Leech",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=unimplemented,
        ),
    ],
)