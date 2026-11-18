from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="6e156ba4-dc2b-5469-90a1-45c56c3c8f5d",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricity.Name",
    display_name="Toxtricity",
    searchable_by=["Toxtricity", "Stage 1", "Toxtricity"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    family_id=848,
    abilities=[
        Attack(
            title="Leer",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Loud Mix",
            game_text="This attack does 30 more damage for each different type of Pok\u00e9mon on your Bench.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)