from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e803e566-b21a-5c5d-a4cd-f2f6dbb93eab",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tirtouga.Name",
    display_name="Tirtouga",
    searchable_by=["Tirtouga", "Stage 1", "Tirtouga"],
    subtypes=["Stage 1"],
    collector_number=106,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AntiqueCoverFossil.Name",
    family_id=564,
    abilities=[
        Attack(
            title="Ancient Seaweed",
            game_text="This attack does 30 damage for each Item card in your opponent's discard pile.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)