from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.attacks_common import discard_for_bonus, smokescreen_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

_provides = lambda type_value: (
    lambda card: energy_provides_type(card, type_value.value)
)


card = PokemonCardDef(
    guid="ab9cf221-8501-5095-88bd-9c6f82627fd1",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareon.Name",
    display_name="Flareon",
    searchable_by=["Flareon", "Stage 1", "Flareon"],
    subtypes=["Stage 1"],
    collector_number=88,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Sand-Attack",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=smokescreen_attack(),
        ),
        Attack(
            title="Fire Slash",
            game_text="You may discard a Fire Energy attached to this Pok\u00e9mon. If you do, this attack does 30 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=discard_for_bonus(
                source="self-energy",
                predicate=_provides(PokemonTypes.FIRE),
                max_count=1,
                flat=30,
            ),
        ),
    ],
)