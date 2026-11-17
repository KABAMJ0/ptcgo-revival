from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8498a04a-4e8a-5701-90dc-7d94d1e9babf",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaCharizardYex.Name",
    display_name="Mega Charizard Y ex",
    searchable_by=["Mega Charizard Y ex", "Stage 2", "MEGA", "ex", "MegaCharizardYex"],
    subtypes=["Stage 2", "MEGA", "ex"],
    collector_number=22,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=360,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Explosion Y",
            game_text="Discard 3 Energy from this Pok\u00e9mon, and this attack does 280 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)