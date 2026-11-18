from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import takes_less_passive

card = PokemonCardDef(
    guid="182d1fa8-7cb5-53a1-91a8-76ad5c9948c8",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bouffalantex.Name",
    display_name="Bouffalant ex",
    searchable_by=["Bouffalant ex", "Basic", "ex", "Bouffalantex"],
    subtypes=["Basic", "ex"],
    collector_number=77,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=626,
    abilities=[
        Ability(
            title="Bouffer",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(30),
        ),
        Attack(
            title="Gold Breaker",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon ex, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)