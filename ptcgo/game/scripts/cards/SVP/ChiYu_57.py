from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="911297b9-3cf8-51af-a0fd-2e9ed05b3e10",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChiYu.Name",
    display_name="Chi-Yu",
    searchable_by=["Chi-Yu", "Basic", "ChiYu"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=1004,
    abilities=[
        Attack(
            title="Flare Bringer",
            game_text="Attach up to 2 Basic Fire Energy cards from your discard pile to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Megafire of Envy",
            game_text="If any of your Pok\u00e9mon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 90 more damage.",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)