from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.card_effects.passives_common import unafflicted
from ptcgo.game.card_effects.support_common import (
    attach_from_hand, hand_attach_condition,
)
from ptcgo.game.card_effects.trainers import basic_energy_of, pokemon_of


WATER_ENERGY = basic_energy_of("water")
WATER_POKEMON = pokemon_of("water")


from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per

card = PokemonCardDef(
    guid="83ce1817-8bcf-50c3-bfea-959b2f7a07a8",
    key="Promo_HGSS",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatr.Name",
    display_name="Feraligatr",
    searchable_by=["Feraligatr", "Stage 2", "Prime", "Feraligatr"],
    subtypes=["Stage 2", "Prime"],
    collector_number=7,
    set_code="Promo_HGSS",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    family_id=160,
    abilities=[
        Ability(
            title="Rain Dance",
            game_text="As often as you like during your turn (before your attack), you may attach a Water Energy from your hand to 1 of your Water Pok\u00e9mon. This power can't be used if Feraligatr is affected by a Special Condition.",
            activation=Activations.UNLIMITED,
            condition=unafflicted,
            effect=attach_from_hand(WATER_ENERGY, target="choice",
                                    target_pred=WATER_POKEMON,
                                    minimum=0),
        ),
        Attack(
            title="Hydro Crunch",
            game_text="Does 60 damage plus 10 more damage for each damage counter on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 4},
            damage=60,
            damage_operator="+",
            effect=damage_per(damage_counters_on("defender"), 10, base=60),
        ),
    ],
)