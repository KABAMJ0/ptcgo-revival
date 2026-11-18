from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7c21f90b-f468-5594-8ac5-e383ce36d260",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spinda.Name",
    display_name="Spinda",
    searchable_by=["Spinda", "Basic", "Spinda"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=327,
    abilities=[
        Attack(
            title="Synchro Removal",
            game_text="If any Energy card attached to Spinda is the same type as any Energy card attached to the Defending Pok\u00e9mon, discard 1 of those Energy cards from the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Pulled Punch",
            game_text="If the Defending Pok\u00e9mon already has any damage counters on it, this attack's base damage is 10 instead of 30.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)