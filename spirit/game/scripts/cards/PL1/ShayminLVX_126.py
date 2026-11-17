from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="abaa5283-2398-5e01-afb4-917f5892834b",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShayminLVX.Name",
    display_name="Shaymin LV.X",
    searchable_by=["Shaymin LV.X", "Level-Up", "ShayminLVX"],
    subtypes=["Level-Up"],
    collector_number=126,
    set_code="PL1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name",
    family_id=492,
    abilities=[
        Ability(
            title="Thankfulness",
            game_text="Each of your Grass Pok\u00e9mon (excluding any Shaymin) gets +40 HP. You can't use more than 1 Thankfulness Pok\u00e9-Body each turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Seed Flare",
            game_text="Choose as many Grass Energy cards from your hand as you like and attach them to your Pok\u00e9mon in any way you like. If you do, this attack does 40 damage plus 20 more damage for each Grass Energy attached in this way.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)