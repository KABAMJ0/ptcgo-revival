from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3dd9cdad-ad00-5e53-b658-a97f3e87b7b2",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Excadrillex.Name",
    display_name="Excadrill ex",
    searchable_by=["Excadrill ex", "Stage 1", "ex", "Excadrillex"],
    subtypes=["Stage 1", "ex"],
    collector_number=160,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    family_id=529,
    abilities=[
        Attack(
            title="Piercing Drill",
            game_text="This attack also does 60 damage to 1 of your opponent's Benched Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Rock Tumble",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=200,
            effect=unimplemented,
        ),
    ],
)