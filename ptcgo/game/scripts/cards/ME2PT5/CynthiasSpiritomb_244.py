from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="cead982a-0ceb-5223-bfe6-3396da011166",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasSpiritomb.Name",
    display_name="Cynthia's Spiritomb",
    searchable_by=["Cynthia's Spiritomb", "Basic", "CynthiasSpiritomb"],
    subtypes=["Basic"],
    collector_number=244,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
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