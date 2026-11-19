from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.card_effects.passives_common import unafflicted
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import move_energy_between
from ptcgo.game.attributes import PokemonTypes


def _grass_energy(card):
    return energy_provides_type(card, PokemonTypes.GRASS.value)


from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6b6938c9-f9bd-5d76-a2f7-bab97c424adc",
    key="Promo_HGSS",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meganium.Name",
    display_name="Meganium",
    searchable_by=["Meganium", "Stage 2", "Prime", "Meganium"],
    subtypes=["Stage 2", "Prime"],
    collector_number=8,
    set_code="Promo_HGSS",
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    family_id=154,
    abilities=[
        Ability(
            title="Leaf Trans",
            game_text="As often as you like during your turn (before your attack), you may move a Grass Energy attached to 1 of your Pok\u00e9mon to another of your Pok\u00e9mon. This power can't be used if Meganium is affected by a Special Condition.",
            activation=Activations.UNLIMITED,
            condition=unafflicted,
            effect=move_energy_between(_grass_energy, count=1),
        ),
        Attack(
            title="Solarbeam",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)