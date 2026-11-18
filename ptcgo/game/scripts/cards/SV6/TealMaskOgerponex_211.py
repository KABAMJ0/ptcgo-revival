from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_per, count_energy
from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.card_effects.support_common import attach_from_hand
from ptcgo.game.card_effects.trainers import basic_energy_of, draw_n

card = PokemonCardDef(
    guid="59eef2a2-636e-53fb-82e1-7c19446d16e9",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TealMaskOgerponex.Name",
    display_name="Teal Mask Ogerpon ex",
    searchable_by=["Teal Mask Ogerpon ex", "Basic", "Tera", "ex", "TealMaskOgerponex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=211,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    abilities=[
        Ability(
            title="Teal Dance",
            game_text="Once during your turn, you may attach a Basic Grass Energy card from your hand to this Pok\u00e9mon. If you attached Energy to a Pok\u00e9mon in this way, draw a card.",
            activation=Activations.ONCE_PER_TURN,
            effect=composed(attach_from_hand(basic_energy_of("grass"), count=1, target="self"), on_success=draw_n(1)),
        ),
        Attack(
            title="Myriad Leaf Shower",
            game_text="This attack does 30 more damage for each Energy attached to both Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 3},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_energy("both"), per=30, base=30),
        ),
    ],
)