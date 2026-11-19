from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_attach_energy, on_bench

def _fairy_energy(card):
    from ptcgo.game.card_effects.pokemon import is_energy_card, energy_provides_type
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FAIRY.value)


card = PokemonCardDef(
    guid="4950da81-018a-5895-af2c-b854eb73a908",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xerneas.Name",
    display_name="Xerneas",
    searchable_by=["Xerneas", "Basic", "Xerneas"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=716,
    abilities=[
        Attack(
            title="Geomancy",
            game_text="Choose 2 of your Benched Pok\u00e9mon. For each of those Pok\u00e9mon, search your deck for a Fairy Energy card and attach it to that Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.FAIRY: 1},
            effect=search_attach_energy(_fairy_energy, 2, to_self=False, distribute=True, target_pred=on_bench),
        ),
        Attack(
            title="Rainbow Spear",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)