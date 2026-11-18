from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.attacks_common import bonus_if, self_energy_discard_attack


def _defender_has_ability(ctx) -> bool:
    return bool(ctx.defender is not None
                and ctx.defender.get_attribute(AttrID.PIE_ABILITIES))

card = PokemonCardDef(
    guid="716075ec-3ba0-526f-87bd-7a4193e7cd93",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningLugia.Name",
    display_name="Shining Lugia",
    searchable_by=["Shining Lugia", "Basic", "ShiningLugia"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=249,
    abilities=[
        Attack(
            title="Argent Wing",
            game_text="If your opponent's Active Pok\u00e9mon has an Ability, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=bonus_if(_defender_has_ability, 60),
        ),
        Attack(
            title="Aero Force",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=130,
            effect=self_energy_discard_attack(1),
        ),
    ],
)