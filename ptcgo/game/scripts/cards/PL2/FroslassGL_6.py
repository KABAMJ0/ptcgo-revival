from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7a0c4812-8440-58d7-970d-ad3fa7432f77",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FroslassGL.Name",
    display_name="Froslass GL",
    searchable_by=["Froslass GL", "Basic", "SP", "FroslassGL"],
    subtypes=["Basic", "SP"],
    collector_number=6,
    set_code="PL2",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=478,
    abilities=[
        Attack(
            title="Sleep Inducer",
            game_text="Switch the Defending Pok\u00e9mon with 1 of your opponent's Benched Pok\u00e9mon. The new Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Wake-Up Slap",
            game_text="If the Defending Pok\u00e9mon is affected by any Special Conditions, this attack does 30 damage plus 20 more damage. Then, remove all Special Conditions from the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)