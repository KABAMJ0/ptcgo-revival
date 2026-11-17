from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7e3e684e-e54d-55fb-8e20-21dcc83f4db6",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensToedscruel.Name",
    display_name="Arven's Toedscruel",
    searchable_by=["Arven's Toedscruel", "Stage 1", "ArvensToedscruel"],
    subtypes=["Stage 1"],
    collector_number=110,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensToedscool.Name",
    family_id=948,
    abilities=[
        Attack(
            title="Pull",
            game_text="Switch in 1 of your opponent's Benched Pok\u00e9mon to the Active Spot.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Reckless Charge",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=unimplemented,
        ),
    ],
)