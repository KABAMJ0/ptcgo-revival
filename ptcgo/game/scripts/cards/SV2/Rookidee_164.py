from ptcgo.game.card_effects.support_common import gust_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="53df3ffd-f401-5045-b0d9-58d8cbd0e2eb",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rookidee.Name",
    display_name="Rookidee",
    searchable_by=["Rookidee", "Basic", "Rookidee"],
    subtypes=["Basic"],
    collector_number=164,
    set_code="SV2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=821,
    abilities=[
        Attack(
            title="Send Back",
            game_text="Switch out your opponent's Active Pok\u00e9mon to the Bench.\u00a0(Your opponent chooses the new Active Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=gust_attack(opponent_chooses=True),
        ),
    ],
)