from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_discard_opponent_energy

card = PokemonCardDef(
    guid="e53a30e2-579c-58ea-b0c4-40b86f6b4d9b",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flapple.Name",
    display_name="Flapple",
    searchable_by=["Flapple", "Stage 1", "Flapple"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    family_id=840,
    abilities=[
        Ability(
            title="Apple Drop",
            game_text="Once during your turn, you may put 2 damage counters on 1 of your opponent's Pok\u00e9mon. If you placed any damage counters in this way, shuffle this Pok\u00e9mon and all attached cards into your deck.",
            effect=flip_gate(discard_opponent_energy_attack(1)),
        ),
        Attack(
            title="Acid Spray",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=flip_discard_opponent_energy(),
        ),
    ],
)