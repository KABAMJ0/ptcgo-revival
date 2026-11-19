from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.card_effects.passives_common import prevent_damage_when
from ptcgo.game.card_effects.pokemon import is_pokemon_vmax

_dauntless_shield = prevent_damage_when(
    lambda calc, c: calc.target is c and calc.attacker is not None
    and is_pokemon_vmax(calc.attacker.archetype_id)
)

card = PokemonCardDef(
    guid="760aba2c-f9ac-59cc-ad33-03e86e4e4d78",
    key="SWSH10TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZamazentaV.Name",
    display_name="Zamazenta V",
    searchable_by=["Zamazenta V", "Basic", "V", "ZamazentaV"],
    subtypes=["Basic", "V"],
    collector_number=22,
    set_code="SWSH10TG",
    rarity=Rarities.RareHoloV,
    hp=230,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=889,
    abilities=[
        Ability(
            title="Dauntless Shield",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon VMAX.",
            passive=_dauntless_shield,
        ),
        Attack(
            title="Assault Tackle",
            game_text="Discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=discard_opponent_energy_attack(special_only=True),
        ),
    ],
)