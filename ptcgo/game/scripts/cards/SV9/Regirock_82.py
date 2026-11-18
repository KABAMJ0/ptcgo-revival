from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import takes_less_passive
from ptcgo.game.card_effects.pokemon import energy_provides_type, is_energy_card
from ptcgo.game.session.effects import is_special_energy
from ptcgo.game.session.passives import carrier_pokemon


def _holder_with(type_value=None, basic_only=False):
    def protects(target, carrier):
        if carrier_pokemon(carrier) is not target:
            return False
        for child in target.children or []:
            if not is_energy_card(child):
                continue
            if basic_only and is_special_energy(child):
                continue
            if type_value is None or energy_provides_type(child, type_value):
                return True
        return False
    return protects

card = PokemonCardDef(
    guid="2e7def90-2108-51e1-ac4c-9fb8218e1dd4",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regirock.Name",
    display_name="Regirock",
    searchable_by=["Regirock", "Basic", "Regirock"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=377,
    abilities=[
        Ability(
            title="Rock Armor",
            game_text="If this Pok\u00e9mon has any Energy attached, it takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(30, protects=_holder_with()),
        ),
        Attack(
            title="Breaching Lariat",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=120,
            effect=unimplemented,
        ),
    ],
)