from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import hp_per_typed_energy_passive



card = PokemonCardDef(
    guid="f0adc3ee-01af-53ac-b2bd-3f7691161ece",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Conkeldurr.Name",
    display_name="Conkeldurr",
    searchable_by=["Conkeldurr", "Stage 2", "Conkeldurr"],
    subtypes=["Stage 2"],
    collector_number=127,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gurdurr.Name",
    family_id=532,
    abilities=[
        Ability(
            title="Craftsmanship",
            game_text="This Pok\u00e9mon gets +40 HP for each Fighting Energy attached to it.",
            passive=hp_per_typed_energy_passive(40, PokemonTypes.FIGHTING.value),
        ),
        Attack(
            title="Swing Around",
            game_text="Flip 2 coins. This attack does 50 more damage for each heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=50),
        ),
    ],
)