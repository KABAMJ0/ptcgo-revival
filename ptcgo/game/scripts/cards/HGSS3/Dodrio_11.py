from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="370d5137-3696-5a7b-9d9d-110abea75bb5",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dodrio.Name",
    display_name="Dodrio",
    searchable_by=["Dodrio", "Stage 1", "Dodrio"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="HGSS3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name",
    family_id=84,
    abilities=[
        Ability(
            title="Retreat Aid",
            game_text="As long as Dodrio is on your Bench, your Active Pok\u00e9mon's Retreat Cost is ColorlessColorless less.",
            effect=unimplemented,
        ),
        Attack(
            title="Incessant Peck",
            game_text="Flip a coin until you get tails. This attack does 20 damage plus 20 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=flip_damage(per_heads=20, until_tails=True, base=20),
        ),
    ],
)