from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.card_effects.passives_common import prevent_damage_when


def _carefree_pred(calc, carrier):
    return calc.is_attack and calc.target is carrier and not calc.to_active

card = PokemonCardDef(
    guid="b10fa22b-ad95-5d6a-8e42-2e1ab351b4b7",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name",
    display_name="Bidoof",
    searchable_by=["Bidoof", "Basic", "Bidoof"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=399,
    abilities=[
        Ability(
            title="Carefree Countenance",
            game_text="As long as this Pok\u00e9mon is on your Bench, prevent all damage done to this Pok\u00e9mon by attacks (both yours and your opponent's).",
            passive=prevent_damage_when(_carefree_pred, attacks_only=False),
        ),
        Attack(
            title="Hyper Fang",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=flip_or_nothing(),
        ),
    ],
)