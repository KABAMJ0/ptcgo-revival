from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cae39fc5-bafa-5a48-9a17-1a247fe63fff",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Loudred.Name",
    display_name="Loudred",
    searchable_by=["Loudred", "Stage 1", "Loudred"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Whismur.Name",
    family_id=293,
    abilities=[
        Attack(
            title="Smash Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Stomp Off",
            game_text="Discard the top card from your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=unimplemented,
        ),
    ],
)