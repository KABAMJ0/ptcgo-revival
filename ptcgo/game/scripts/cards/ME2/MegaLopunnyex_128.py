from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="4f2837be-a8ab-5eb3-8ce0-75075d707fc2",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaLopunnyex.Name",
    display_name="Mega Lopunny ex",
    searchable_by=["Mega Lopunny ex", "Stage 1", "MEGA", "ex", "MegaLopunnyex"],
    subtypes=["Stage 1", "MEGA", "ex"],
    collector_number=128,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name",
    family_id=427,
    abilities=[
        Attack(
            title="Gale Thrust",
            game_text="If this Pok\u00e9mon moved from your Bench to the Active Spot this turn, this attack does 170 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Spiky Hopper",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
    ],
)