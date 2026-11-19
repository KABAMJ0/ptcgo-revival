from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.card_effects.attacks_common import bonus_if, has_damage
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack, condition_attack

card = PokemonCardDef(
    guid="2b5612aa-a9c8-5704-87e6-9f3f09f1906b",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WhiteKyuremGX.Name",
    display_name="White Kyurem-GX",
    searchable_by=["White Kyurem-GX", "Basic", "GX", "WhiteKyuremGX"],
    subtypes=["Basic", "GX"],
    collector_number=141,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=646,
    abilities=[
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
        Attack(
            title="Raging Blade",
            game_text="If this Pok\u00e9mon has any damage counters on it, this attack does 80 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=bonus_if(has_damage('self'), 80),
        ),
        Attack(
            title="Dragon Nova-GX",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned and Paralyzed. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=condition_attack(SpecialConditions.BURNED, SpecialConditions.PARALYZED),
        ),
    ],
)