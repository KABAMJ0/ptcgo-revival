from ptcgo.game.card_effects.support_common import draw_until_effect
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_until_effect

card = PokemonCardDef(
    guid="fff5dbfd-9f08-51c9-a573-ebc532443012",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LickilickyC.Name",
    display_name="Lickilicky C",
    searchable_by=["Lickilicky C", "Basic", "SP", "LickilickyC"],
    subtypes=["Basic", "SP"],
    collector_number=30,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=463,
    abilities=[
        Attack(
            title="Licking-Licking Heal",
            game_text="Attach a Basic Energy card from your hand to 1 of your Pok\u00e9mon. Then, remove 2 damage counters from that Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Return",
            game_text="Draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=draw_until_effect(6),
        ),
    ],
)