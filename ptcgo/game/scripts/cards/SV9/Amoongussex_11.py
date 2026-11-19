from ptcgo.game.card_effects.attacks_common import condition_attack, flip_bonus
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="a65caa4c-d5c6-5121-a42e-811e980a8483",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Amoongussex.Name",
    display_name="Amoonguss ex",
    searchable_by=["Amoonguss ex", "Stage 1", "ex", "Amoongussex"],
    subtypes=["Stage 1", "ex"],
    collector_number=11,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name",
    family_id=590,
    abilities=[
        Attack(
            title="Spore Ball",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Champignon's Swing",
            game_text="Flip a coin. If heads, this attack does 80 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=flip_bonus(80),
        ),
    ],
)