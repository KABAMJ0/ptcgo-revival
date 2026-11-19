from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import gust_attack

card = PokemonCardDef(
    guid="6374d0d0-f3b5-57e7-a127-51c5b84e1b48",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchling.Name",
    display_name="Fletchling",
    searchable_by=["Fletchling", "Basic", "Fletchling"],
    subtypes=["Basic"],
    collector_number=121,
    set_code="SV7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=661,
    abilities=[
        Attack(
            title="Send Back",
            game_text="Switch out your opponent's Active Pok\u00e9mon to the Bench. (Your opponent chooses the new Active Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=gust_attack(opponent_chooses=True),
        ),
    ],
)