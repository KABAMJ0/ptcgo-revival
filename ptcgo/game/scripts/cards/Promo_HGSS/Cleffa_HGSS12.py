from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID
from ptcgo.game.session.passives import Passive, carrier_pokemon
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

class AsleepShieldPassive(Passive):
    """While the holder is Asleep, attacks do it no damage at all."""

    def prevents_damage(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if not (calc.is_attack and calc.is_opposing) or holder is None:
            return False
        if calc.target is not holder:
            return False
        conditions = holder.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
        labels = {str(label).lower() for label in conditions}
        return "asleep" in labels


card = PokemonCardDef(
    guid="46603c27-5db2-577f-ba3c-11467787bae8",
    key="Promo_HGSS",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cleffa.Name",
    display_name="Cleffa",
    searchable_by=["Cleffa", "Basic", "Cleffa"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="Promo_HGSS",
    rarity=Rarities.RarePromo,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=173,
    abilities=[
        Ability(
            title="Sweet Sleeping Face",
            game_text="As long as Cleffa is Asleep, prevent all damage done to Cleffa by attacks.",
            passive=AsleepShieldPassive(),
        ),
        Attack(
            title="Eeeeeeek",
            game_text="Shuffle your hand into your deck, then draw 6 cards. Cleffa is now Asleep.",
            cost={},
            effect=unimplemented,
        ),
    ],
)