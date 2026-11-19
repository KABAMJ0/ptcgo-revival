from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import choose_attack_lock

card = PokemonCardDef(
    guid="d6b0e516-541a-5e30-a59b-0d45aa3afe49",
    key="GUM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name",
    display_name="Mewtwo",
    searchable_by=["Mewtwo", "Basic", "Mewtwo"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="GUM",
    rarity=Rarities.RareUltra,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Psyjack",
            game_text="Choose 1 of your opponent's Active Pok\u00e9mon's attacks. That Pok\u00e9mon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=choose_attack_lock(),
        ),
        Attack(
            title="Break Burn",
            game_text="Discard 2 Psychic Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=self_energy_discard_attack(count=2, energy_type=PokemonTypes.PSYCHIC),
        ),
    ],
)