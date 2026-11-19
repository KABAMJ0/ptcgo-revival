from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="42d9e595-f208-5f6d-b58d-b98c31e278f8",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrogue.Name",
    display_name="Tyrogue",
    searchable_by=["Tyrogue", "Basic", "Tyrogue"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="COL",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=236,
    abilities=[
        Ability(
            title="Sweet Sleeping Face",
            game_text="As long as Tyrogue is Asleep, prevent all damage done to Tyrogue by attacks.",
            effect=unimplemented,
        ),
        Attack(
            title="Mischievous Punch",
            game_text="This attack's damage isn't affected by Weakness or Resistance. Tyrogue is now Asleep.",
            cost={},
            damage=30,
            effect=composed(
                ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True),
                then=lambda ctx: ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP),
            ),
        ),
    ],
)