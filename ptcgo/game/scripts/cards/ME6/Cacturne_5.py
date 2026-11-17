from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a31e6d22-d2b3-52cc-81d0-4aebd84d1ac8",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cacturne.Name",
    display_name="Cacturne",
    searchable_by=["Cacturne", "Stage 1", "Cacturne"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="ME6",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name",
    family_id=331,
    abilities=[
        Attack(
            title="Linear Attack",
            game_text="This attack does 30 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Punishing Needles",
            game_text="This attack does 50 more damage for each of your opponent's Pok\u00e9mon in play that has an Ability.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)