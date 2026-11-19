from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.card_effects.attacks_common import count_hand, damage_per
from ptcgo.game.card_effects.support_common import draw_attack
card = PokemonCardDef(
    guid="86015a71-a6eb-5706-adc6-bc78bc4f67cb",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatonex.Name",
    display_name="Tinkaton ex",
    searchable_by=["Tinkaton ex", "Stage 2", "ex", "Tinkatonex"],
    subtypes=["Stage 2", "ex"],
    collector_number=31,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=300,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name",
    family_id=959,
    abilities=[
        Attack(
            title="Big Hammer",
            game_text="This attack does 30 damage for each card in your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_hand("mine"), 30),
        ),
        Attack(
            title="Pulverizing Press",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
    ],
)