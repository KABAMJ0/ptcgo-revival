from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_attack
from ptcgo.game.card_effects.passives_common import trainer_effect_shield_passive
from ptcgo.game.session.passives import carrier_pokemon


def _benched_basic(entity, carrier):
    # Attachments count as effects done to the Pokemon they ride under.
    holder = carrier_pokemon(entity) if entity is not None else None
    if holder is None:
        return False
    parent = getattr(holder, "parent", None)
    return (
        bool(parent) and parent.get_attribute(AttrID.NAME) == "bench"
        and holder.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
    )

card = PokemonCardDef(
    guid="042ee622-d3c1-5e68-968b-36d5145293c0",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Diancie.Name",
    display_name="Diancie",
    searchable_by=["Diancie", "Basic", "Diancie"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=719,
    abilities=[
        Ability(
            title="Princess's Curtain",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, whenever your opponent plays a Supporter card from their hand, prevent all effects of that card done to your Benched Basic Pok\u00e9mon.",
            passive=trainer_effect_shield_passive(
                protects=_benched_basic, while_active=True),
        ),
        Attack(
            title="Spike Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=draw_attack(2),
        ),
    ],
)