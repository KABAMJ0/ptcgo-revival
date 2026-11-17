from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3eb53f69-2380-5a61-b2c0-1cf78085f4a5",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gorebyss.Name",
    display_name="Gorebyss",
    searchable_by=["Gorebyss", "Stage 1", "Gorebyss"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name",
    family_id=366,
    abilities=[
        Attack(
            title="Crescendo Wave",
            game_text="This attack does 30 damage for each Water Energy attached to this Pok\u00e9mon. Before doing damage, you may attach any number of Basic Water Energy cards from your hand to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)