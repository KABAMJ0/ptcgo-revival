from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.attacks_common import no_retreat_attack
from ptcgo.game.card_effects.passives_common import takes_less_passive
from ptcgo.game.session.constants import BENCH_CAPACITY


def _at_full_hp(target, carrier) -> bool:
    remaining = target.get_attribute(AttrID.HP, 0)
    return (target is carrier
            and remaining == target.attribute_originals.get(AttrID.HP.value, remaining))

card = PokemonCardDef(
    guid="6d49c709-36f0-5e9b-bc64-c132bdb29805",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CarracostaGX.Name",
    display_name="Carracosta-GX",
    searchable_by=["Carracosta-GX", "Stage 2", "GX", "CarracostaGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=239,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tirtouga.Name",
    family_id=565,
    abilities=[
        Ability(
            title="High Density Armor",
            game_text="If this Pok\u00e9mon has full HP, it takes 90 less damage from your opponent's attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(90, protects=_at_full_hp),
        ),
        Attack(
            title="Ground Crush",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=no_retreat_attack(),
        ),
        Attack(
            title="Stone Age-GX",
            game_text="Put any number of Pok\u00e9mon that evolve from Unidentified Fossil from your discard pile onto your Bench. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)