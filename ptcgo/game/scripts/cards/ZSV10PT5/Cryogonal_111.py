from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import gust_attack

card = PokemonCardDef(
    guid="5b7c8d99-fd02-556f-a542-fc68733531e9",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cryogonal.Name",
    display_name="Cryogonal",
    searchable_by=["Cryogonal", "Basic", "Cryogonal"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=615,
    abilities=[
        Attack(
            title="Drag Off",
            game_text="Switch in 1 of your opponent's Benched Pok\u00e9mon to the Active Spot. This attack does 20 damage to the new Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            effect=gust_attack(damage_to_new_active=20),
        ),
        Attack(
            title="Icicle",
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
    ],
)