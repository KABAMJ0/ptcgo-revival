from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.session.effects import is_special_energy
from ptcgo.game.card_effects.attacks_common import discard_for_bonus, smokescreen_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import smokescreen_attack


card = PokemonCardDef(
    guid="dcf08b92-6ed3-561a-8a4b-c861d210bc11",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Octillery.Name",
    display_name="Octillery",
    searchable_by=["Octillery", "Stage 1", "Octillery"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="SM4",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    family_id=223,
    abilities=[
        Attack(
            title="Ink Spit",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=smokescreen_attack(),
        ),
        Attack(
            title="Special Artillery",
            game_text="You may discard a Special Energy from this Pok\u00e9mon. If you do, this attack does 80 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=discard_for_bonus(
                source="self-energy",
                predicate=is_special_energy,
                max_count=1,
                flat=80,
            ),
        ),
    ],
)