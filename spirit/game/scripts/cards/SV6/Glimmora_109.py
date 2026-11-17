from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b0d428a0-92ac-55d3-b711-6cd0bd552655",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmora.Name",
    display_name="Glimmora",
    searchable_by=["Glimmora", "Stage 1", "Glimmora"],
    subtypes=["Stage 1"],
    collector_number=109,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmet.Name",
    family_id=969,
    abilities=[
        Attack(
            title="Stun Poison",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Venoshock",
            game_text="If your opponent's Active Pok\u00e9mon is Poisoned, this attack does 100 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)