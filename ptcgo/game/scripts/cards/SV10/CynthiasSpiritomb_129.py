from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="053247e3-66eb-5911-b7e6-6f612d42000b",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasSpiritomb.Name",
    display_name="Cynthia's Spiritomb",
    searchable_by=["Cynthia's Spiritomb", "Basic", "CynthiasSpiritomb"],
    subtypes=["Basic"],
    collector_number=129,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=442,
    abilities=[
        Attack(
            title="Raging Curse",
            game_text="This attack does 10 damage for each damage counter on all of your Benched Cynthia's Pok\u00e9mon. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=ignore_modifier_attack(ignore_weakness=True),
        ),
    ],
)