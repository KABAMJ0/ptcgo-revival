from ptcgo.game.card_effects.attacks_common import reduce_defender_attacks
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import reduce_defender_attacks

card = PokemonCardDef(
    guid="1946b2d1-4cd0-5e3c-bfe7-cfb82d24896b",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name",
    display_name="Buneary",
    searchable_by=["Buneary", "Basic", "Buneary"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="ME1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=427,
    abilities=[
        Attack(
            title="Charm",
            game_text="During your opponent's next turn, attacks used by the Defending Pok\u00e9mon do 20 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=reduce_defender_attacks(20),
        ),
        Attack(
            title="Skip",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)