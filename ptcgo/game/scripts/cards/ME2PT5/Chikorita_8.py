from ptcgo.game.card_effects.attacks_common import reduce_defender_attacks
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import reduce_defender_attacks

card = PokemonCardDef(
    guid="d54c45ab-200b-5e14-92ef-0cdd2f8d3733",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chikorita.Name",
    display_name="Chikorita",
    searchable_by=["Chikorita", "Basic", "Chikorita"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=152,
    abilities=[
        Attack(
            title="Growl",
            game_text="During your opponent's next turn, attacks used by the Defending Pok\u00e9mon do 20 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=reduce_defender_attacks(20),
        ),
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
        ),
    ],
)