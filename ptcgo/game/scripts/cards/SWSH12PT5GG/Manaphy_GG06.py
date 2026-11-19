from ptcgo.game.card_effects.pokemon import WaveVeilPassive
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="34ec0c72-e492-5d78-a3cd-f7ab5cb10041",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name",
    display_name="Manaphy",
    searchable_by=["Manaphy", "Basic", "Manaphy"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=490,
    abilities=[
        Ability(
            title="Wave Veil",
            game_text="Prevent all damage done to your Benched Pokémon by attacks from your opponent's Pokémon.",
            passive=WaveVeilPassive(),
        ),
        Attack(
            title="Rain Splash",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)
