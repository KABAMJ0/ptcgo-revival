from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6599d706-552f-5582-af6f-c1e0a7e29e8c",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marshtomp.Name",
    display_name="Marshtomp",
    searchable_by=["Marshtomp", "Stage 1", "Marshtomp"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mudkip.Name",
    family_id=258,
    abilities=[
        Ability(
            title="Plunge",
            game_text="Once during your turn (before your attack), if Marshtomp is on your Bench, you may flip a coin. If heads, move all Energy cards attached to your Active Pok\u00e9mon to Marshtomp. If you do, switch Marshtomp with that Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Mud Shot",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)