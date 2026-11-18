from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7e8ce22b-bc0e-5bc4-8cc5-9073d327fa36",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TingLu.Name",
    display_name="Ting-Lu",
    searchable_by=["Ting-Lu", "Basic", "TingLu"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=1003,
    abilities=[
        Attack(
            title="Ground Crasher",
            game_text="If a Stadium is in play, this attack also does 30 damage to each of your opponent's Benched Pok\u00e9mon, and discard that Stadium. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)